import { useParams } from "react-router";
import useR from "./useR.js";
import { useHistory } from "react-router-dom";

const BlogDetail = () => {
    const { id } = useParams();
    const history = useHistory();
    const {data: blog, isLoading, error} = useR('http://localhost:8000/blogs/'+id);
    const HandleDelete= () => {
        fetch('http://localhost:8000/blogs/'+id,{
            method: 'DELETE'
        }).then( () => {
            console.log('Succes!');
            history.push('/');
        })
    }
    return ( 
        <div className="">
            {isLoading && <div>En cour de traitement...</div>}
            {error && <div style={ {'color': 'red'}}>{error}</div>}
            { blog && (
                <div className="blog">
                    <h2 className="blog-titre">{blog.title}</h2>
                    <small className="blog-publication-date">{`Publier le: ${blog.date}`}</small>
                    <p className="blog-body">{blog.body}</p>
                    <p className="blog-author">{`Publier par: ${blog.author}`}</p>
                <button onClick={HandleDelete} className="buttonArticle">Supprimer</button>
                </div>
            ) }
        </div>
     );
}
 
export default BlogDetail;