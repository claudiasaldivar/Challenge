import { useState, useEffect } from "react"
import { getStore, getFilms } from "../services/services"
import { createInventory, getInventory, updateInventory } from "../services/services"

const FormularioInventario = (props) => {
    const [stores, setStores] = useState(null)
    const [filmes, setFilmes] = useState(null)
    const [storeId, setStoreId] = useState(null)
    const [filmId, setFilmId] = useState(null)

    const { inventory, setInventory, update, inventario, setInventario} = props
    useEffect( () => {
        async function fetchData() {
            const storesData = await getStore()
            const filmsData = await getFilms()
            const inventoryData = await getInventory()
            setStores(storesData)
            setFilmes(filmsData)
            setInventory(inventoryData)
        }
          fetchData();
        
      }, []);

      const handleSubmit = async (e) => {
        e.preventDefault();
        
        if([storeId, filmId].includes('')){
            return
        }
        const objetoInvetory = {
            store: stores[0].id,
            film: filmes[0].id
        }
       
        const create = await createInventory(objetoInvetory) 
        setInventory([...inventory, create]) 
        setFilmId('')
        setStoreId('')
    }

    const handleUpdate = async (e) => {
        e.preventDefault();
        
        const objetoInvetory = {
            store: stores[0].id,
            film: filmes[0].id
        }
       
        const update = await updateInventory(objetoInvetory, inventario.id) 
        setInventory([...inventory, update]) 
        setFilmId('')
        setStoreId('')
    }
    
  return (
    <div className="md:w-1/2 lg:w-2/5">
        <h2 className="font-black text-white text-3xl text-center">Inventario</h2>
        <p className="text-white text-lg mt-5 text-center mb-10">
            Añade Inventario y {""}
            <span className="text-indigo-400 font-bold">Administralos</span>
        </p>
        <form className="bg-white shadow-md rounded-lg py-10 px-5 mb-10 mx-5" onSubmit={inventario?.id ? handleUpdate : handleSubmit}>
            <div className="mb-2">
                <label htmlFor="tienda" className="block text-gray-700 uppercase font-bold">Tienda</label>
                <select 
                    id='tienda' 
                    value={storeId} 
                    onChange={(e) => Number(setStoreId(e.target.value))} 
                    className="border-2 w-full p-2 mt-2 placeholder-gray-100 rounded-md"
                >
                    <option value=''>       --Seleccione--      </option>
                    {stores?.map((store) => (
                        <option value={store} key={store.id}>{store.id}</option>
                    ))}
                </select>
            </div>
            <div className="mb-5">
                <label htmlFor="film" className="block text-gray-700 uppercase font-bold">Film</label>
                <select 
                    id='film' 
                    value={filmId} 
                    className="border-2 w-full p-2 mt-2 placeholder-gray-100 rounded-md" 
                    onChange={(e) => Number(setFilmId(e.target.value))}
                    >
                    <option value=''>       --Seleccione--      </option>
                    {filmes?.map((film) => (
                        <option value={film?.title} key={film?.id}>{film?.title}</option>
                    ))}
                </select>
            </div>
            <input 
                className="bg-indigo-600 w-full p-3 text-white uppercase font-bold hover:bg-indigo-700 cursor-pointer transition-all"
                type="submit"
                value={inventario?.id ? "Edita inventario" : "Agrega inventario"}
                />
            </form>
        </div>
  )
}

export default FormularioInventario