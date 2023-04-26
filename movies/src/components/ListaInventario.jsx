import Card from "./Inventario";

const Listado = ({inventario, deleteItem, setInvetario}) => {

    return ( 
        <div className="md:w-1/2 lg:w-3/5 md:h-screen overflow-y-scroll">
        {inventario && inventario.length ? (
            <>
            <h2 className="font-black text-white text-3xl text-center">
                Inventario
            </h2>
            <p className="text-white text-xl mt-5 mb-10 text-center">
                Administra tu {""}
                <span className="text-indigo-300 font-bold ">Inventario</span>
            </p>
            {inventario?.map((item) => <Card key={item.id} item={item} deleteItem={deleteItem} setInvetario={setInvetario}/>)}
        
            </>
        ): (
           <>
           <h2 className="font-black text-3xl text-center">
                No hay pacientes
            </h2>
            <p className="text-xl mt-5 mb-10 text-center">
                Empieza agregando y apareceran {""}
                <span className="text-indigo-600 font-bold ">en este lugar</span>
            </p>
           </>
            )}
        </div>  
     );
}
 
export default Listado;