import { BrowserRouter, Routes, Route } from "react-router-dom";
import Header from "./components/Header";
import Hero from "./components/Hero";
import Home from "./components/Home";
import HeroPowerForm from "./components/HeroPowerForm";
import Power from "./components/Power";
import PowerEditForm from "./components/PowerEditForm";
import PowerById from "./components/PowerById";

function App() {
  return (
    <BrowserRouter>
    <div>
      <Header />
      <main>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/hero_powers/new" element={<HeroPowerForm />} />
          <Route path="/powers/:id/edit" element={<PowerEditForm />} />
          <Route path="/powers" element={<Power />} />
          <Route path="/heroes/:id" element={<Hero />} />
          <Route path="/powers/:id" element={<PowerById />} />
        </Routes>
      </main>
    </div>
    </BrowserRouter>
  );
}

export default App;