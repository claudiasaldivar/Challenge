
const Card = ({item, deleteItem, setInvetario}) => {

    const {store, film, last_update, id} = item

    const handleDelete = () => {
        const respuesta = confirm('Deseas eliminar')
        if(respuesta){
            deleteItem(id)
        }

    }
  return (
    <div className="mx-5 my-10 bg-white shadow-md px-5 py-10 rounded-xl">
    <p className="font-bold mb-3 text-gray-700 uppercase">
    ID: {""}
        <span className="font-normal normal-case">{id}</span>
    </p>
    <p className="font-bold mb-3 text-gray-700 uppercase">
    Store: {""}
        <span className="font-normal normal-case">{store}</span>
    </p>
    <p className="font-bold mb-3 text-gray-700 uppercase">
    Film: {""}
        <span className="font-normal normal-case">{film}</span>
    </p>
    <p className="font-bold mb-3 text-gray-700 uppercase">
    Last update: {""}
        <span className="font-normal normal-case">{last_update}</span>
    </p>
    <div className="flex justify-between mt-10">
        <button type="button" 
            className="py-2 px-10 bg-indigo-600 hover:bg-indigo-700 text-white font-bold rounded-lg"
            onClick={() => setInvetario(item)}
            >
            Editar
        </button>
        <button type="button" 
        className="py-2 px-10 bg-red-600 hover:bg-red-700 text-white font-bold rounded-lg"
        onClick={() =>handleDelete()}
        >Eliminar</button>
    </div>
</div>
  )
}

export default Card