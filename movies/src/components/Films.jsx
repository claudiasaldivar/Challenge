
const Filmes = ({filmes}) => {

    return (
      <div className="md:w-1/2 lg:w-3/5 md:h-screen overflow-y-scroll">
      {filmes && filmes.length ? (
          <>
          <h2 className="font-black text-white text-3xl text-center">
              Inventario
          </h2>
          <p className="text-white text-xl mt-5 mb-10 text-center">
              Administra tu {""}
              <span className="text-indigo-300 font-bold ">Inventario</span>
          </p>
          {filmes?.map((item) => (
              <div className="mx-5 my-10 bg-white shadow-md px-5 py-10 rounded-xl" key={item.id}>
                  <p className="font-bold mb-3 text-gray-700 uppercase">
                  Title: {""}
                      <span className="font-normal normal-case">{item.title}</span>
                  </p>
                  <p className="font-bold mb-3 text-gray-700 uppercase">
                Description: {""}
                      <span className="font-normal normal-case">{item.description}</span>
                  </p>
                  <p className="font-bold mb-3 text-gray-700 uppercase">
                  Release Year: {""}
                      <span className="font-normal normal-case">{item.release_year}</span>
                  </p>
                  <p className="font-bold mb-3 text-gray-700 uppercase">
                  Rating: {""}
                      <span className="font-normal normal-case">{item.rating}</span>
                  </p>
                  <p className="font-bold mb-3 text-gray-700 uppercase">
                  Fulltext: {""}
                      <span className="font-normal normal-case">{item.fulltext}</span>
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
  
  export default Filmes