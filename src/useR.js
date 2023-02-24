import { useState, useEffect } from "react";

const useR = (url) => {

    const [data,setData]= useState(null);
    const [isLoading, setIsLoading]= useState(true);
    const [error,setError]= useState(null);
      
    useEffect( () => {
      const abortCont = new AbortController();
        setTimeout( () => {
          fetch(url,{signal: abortCont.signal})
          .then((response) => {
              if(!response.ok){
                  throw Error('Désoler, une érreur est survenue');
              }
              return response.json()
          })
          .then((data) => {
              console.log(data);
              setData(data);
              setIsLoading(false);
              setError(null);
          })
          .catch( err =>{
            if (err.name ==="AbortError") {
              console.log("le chargement a été stoper");
            }else{
              console.log(err);
              setError(err.message);
              setIsLoading(false);
            }

          })
            
      },100);

        return () => abortCont.abort();

      },[url]);
    return {data,isLoading,error};
}
 
export default useR;