import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

function Home() {
  const [heros, setHeros] = useState([]);

  useEffect(() => {
    fetch("/api/heroes")
      .then((res) => res.json())
      .then((responseData) => {
        console.log(responseData);
        setHeros(responseData);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }, []);

  return (
    <section>
      <h2>All Heroes</h2>
      <ul>
        {Array.isArray(heros) ? (
          heros.map((hero) => (
            <li key={hero.id}>
              <Link to={`/heroes/${hero.id}`}>{hero.super_name}</Link>
            </li>
          ))
        ) : (
          <p>Loading...</p>
        )}
      </ul>
    </section>
  );
}

export default Home;
