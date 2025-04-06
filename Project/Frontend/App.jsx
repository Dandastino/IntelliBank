import React, { useState, useEffect } from "react";
import * as d3 from "d3";

function QuantityChart({ data }) {
  useEffect(() => {
    // Genera grafico
  }, [data]);
  return <svg width={500} height={300}></svg>;
}

export default function App() {
  const [data, setData] = useState({});
  useEffect(() => {
    fetch("http://127.0.0.1:8000/analyze/")
      .then((res) => res.json())
      .then((data) => setData(data));
  }, []);
  return <QuantityChart data={data} />;
}
