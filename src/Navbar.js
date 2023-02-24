const Navbar = () => {
  return (
    <nav className="navbar">
      <div>
        <a className="logo" href="/">Blog</a>
      </div>
      <ul className="liens">
        <li>
          <a href="/" className="lien">Acceuil</a>
        </li>
        <li>
          <a href="/ajouter" className="lien buttonArticle" >Creer Article</a>
        </li>
      </ul>
    </nav>
  );
};
export default Navbar;
