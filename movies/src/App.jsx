import { useState, useEffect } from "react"
import Navbar from "./components/Navbar"
import FormularioInventario from "./components/FormularioInventario"
import Listado from "./components/ListaInventario"
import Clientes from "./components/Clientes"
import { deleteInventory, getClients, getFilms } from "../src/services/services"
import Filmes from "./components/Films"

function App() {
  const [inventory, setInventory] = useState([]) 
  const [invetario, setInvetario] = useState({})
  const [openInventario, setOpenInventario] = useState(true)
  const [openFilms, setOpenFilms] = useState(false)
  const [openClientes, setOpenClientes] = useState(false)
  const [clientes, setClientes] = useState(null)
  const [filmes, setFilmes] = useState(null)

  const deleteItem = (id) => {
    deleteInventory(id)
    setInventory(inventory.filter((invetoryState) => invetoryState.id !== id))
  }

useEffect(() => {
  async function fetchData() {
    const response = await getClients();
    setClientes(response)
  }
  fetchData();
}, [openClientes]);

useEffect( () => {
  async function fetchData() {

      const filmsData = await getFilms()
      setFilmes(filmsData)

  }
    fetchData();
  
}, [openFilms]);


  
  return (
    <div className="container mx-auto mt-5">
      <Navbar 
        setOpenInventario={setOpenInventario}
        setOpenFilms={setOpenFilms}
        setOpenClientes={setOpenClientes}
      />
      {openInventario && (
        <div className="mt-12 md:flex">
        <FormularioInventario setInventory={setInventory} inventory={inventory} inventario={invetario} setInventario={setInvetario}/>
        <Listado inventario={inventory} deleteItem ={deleteItem} setInvetario={setInvetario} />
      </div>
      )}
      {openFilms && (
        <div className="mt-12 md:flex justify-center">
        <Filmes filmes={filmes} />
      </div>
      )}
      {openClientes && (
        <div className="mt-12 md:flex justify-center">
        <Clientes clientes={clientes} />
      </div>
      )}
    </div>
  )
}

export default App
