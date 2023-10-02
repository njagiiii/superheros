import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

function Power() {
  const [powers, setPowers] = useState([]);

  useEffect(() => {
    fetch("/api/powers")
      .then((res) => res.json())
      .then((responseData) => {
        console.log(responseData);
        setPowers(responseData);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }, []);

  return (
    <section>
      <h2>All Powers</h2>
      <ul>
        {powers.map((power) => (
          <li key={power.id}>
            <h3>{power.name}</h3>
            <p>{power.description}</p>
            <p>
        <Link to={`/powers/${power.id}/edit`}>Edit Power Description</Link>
      </p>
          </li>

        ))}
      </ul>
      <p>
        <Link to="/hero_powers/new">Add Hero Power</Link>
      </p>
      
    </section>
  );
}

export default Power;