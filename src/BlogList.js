const BlogList = ({blogs,title}) => {

    return ( 
        <div className="bloglist">
            <h2 className="blog-titre">{title}</h2>
            {
                blogs.map( (blog) => (
                    <div className="blog" key={blog.id}>
                        <a href={`/blogs/${blog.id}`} className="blog-titre">{blog.title}</a>
                        <small className="blog-publication-date">Publier le: {blog.date}</small>
                        <p className="blog-author">Publier par: {blog.author}</p>
                    </div>
                ))
            }
        </div>
     );
}
 
export default BlogList;