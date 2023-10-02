import React, { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";

function Hero() {
  const [hero, setHero] = useState(null);
  const [error, setError] = useState(null);
  const [status, setStatus] = useState("pending");
  const { id } = useParams();

  useEffect(() => {
    fetch(`/api/heroes/${id}`)
      .then((r) => {
        if (r.ok) {
          r.json().then((hero) => {
            setHero(hero);
            setError(null);
            setStatus("resolved");
          });
        } else {
          r.json().then((err) => {
            setHero(null);
            setError(err.error);
            setStatus("rejected");
          });
        }
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
        setHero(null);
        setError("Network Error");
        setStatus("rejected");
      });
  }, [id]);

  if (status === "pending") return <h1>Loading...</h1>;
  if (status === "rejected") return <h1>Error: {error}</h1>;

  // Check if hero is available before rendering hero details
  if (!hero) return null;

  return (
    <section>
      <h2>{hero.super_name}</h2>
      <h2>AKA {hero.name}</h2>

      <h3>Powers:</h3>
      <ul>
      {hero.hero_powers.map((heroPower) => (
          <li key={heroPower.id}>
            Name: {heroPower.power.name}<br></br>
            Strength: {heroPower.strength}
          </li>
        ))}
      </ul>

      <Link to="/hero_powers/new">Add Hero Power</Link>
    </section>
  );
}

export default Hero;