import React, { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";

function PowerById() {
  const [power, setPower] = useState(null);
  const [error, setError] = useState(null);
  const [status, setStatus] = useState("pending");
  const { id } = useParams();

  useEffect(() => {
    fetch(`/api/powers/${id}`)
      .then((r) => {
        if (r.ok) {
          r.json().then((hero) => {
            setPower(hero);
            setError(null);
            setStatus("resolved");
          });
        } else {
          r.json().then((err) => {
            setPower(null);
            setError(err.error);
            setStatus("rejected");
          });
        }
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
        setPower(null);
        setError("Network Error");
        setStatus("rejected");
      });
  }, [id]);

  if (status === "pending") return <h1>Loading...</h1>;
  if (status === "rejected") return <h1>Error: {error}</h1>;

  // Check if hero is available before rendering hero details
  if (!power) return null;

  return (
    <section>
      <h2>{power.name}</h2>
      <h2>AKA {power.description}</h2>
    </section>
  );
}

export default PowerById;