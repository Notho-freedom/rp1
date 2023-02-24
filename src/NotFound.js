import { Link } from "react-router-dom";

const NotFound = () => {
    return (
        <div className="404">
            <h2>Ooooups......</h2>
            <p> la page que vous essayez de rejoindre n'existe pas</p>
            <h4><a href="/">Retournez à la page d Acceuil!</a></h4>
            <Link to='/'>Acceuil</Link>
        </div>
     );
}
 
export default NotFound;