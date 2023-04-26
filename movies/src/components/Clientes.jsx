
const Clientes = ({clientes}) => {

  return (
    <div className="md:w-1/2 lg:w-3/5 md:h-screen overflow-y-scroll">
    {clientes && clientes.length ? (
        <>
        <h2 className="font-black text-white text-3xl text-center">
            Inventario
        </h2>
        <p className="text-white text-xl mt-5 mb-10 text-center">
            Administra tu {""}
            <span className="text-indigo-300 font-bold ">Inventario</span>
        </p>
        {clientes?.map((item) => (
            <div className="mx-5 my-10 bg-white shadow-md px-5 py-10 rounded-xl" key={item.id}>
                <p className="font-bold mb-3 text-gray-700 uppercase">
                Name: {""}
                    <span className="font-normal normal-case">{item.first_name}</span>
                </p>
                <p className="font-bold mb-3 text-gray-700 uppercase">
               Last Name: {""}
                    <span className="font-normal normal-case">{item.last_name}</span>
                </p>
                <p className="font-bold mb-3 text-gray-700 uppercase">
                Email: {""}
                    <span className="font-normal normal-case">{item.email}</span>
                </p>
                <p className="font-bold mb-3 text-gray-700 uppercase">
                Address: {""}
                    <span className="font-normal normal-case">{item.address}</span>
                </p>
                <p className="font-bold mb-3 text-gray-700 uppercase">
                Store: {""}
                    <span className="font-normal normal-case">{item.store}</span>
                </p>
            </div>
        ))}
    
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
    
  )
}

export default Clientes