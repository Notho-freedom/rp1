import useR from './useR';
import BlogList from './BlogList';

const Home = () => {

    const {data:blogs, isLoading,error} = useR('http://localhost:8000/blogs?_sort=id&_order=desc');
    return ( 
    <div className="home">
        {error && <div style={{"color":"red"}}>{error}</div> }
        {isLoading && <div>Chargement...</div>}
    { blogs && <BlogList blogs={blogs} title={'Listes Des Blogs'} />}
    </div>
     );
}
 
export default Home;