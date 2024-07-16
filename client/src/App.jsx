import { useEffect, useState } from "react";
import axios from "axios";
import URL from "./URL";

export default function App() {
  const [data, setData] = useState("");
  const Data = async () => {
    try {
      const response = await axios.get(URL.base);
      setData(response.data);
    } catch (error) {
      console.log(error);
    }
  };
  useEffect(() => {
    Data();
  }, []);
  return (
    <>
      <div className="">Wael Alturi</div>
    </>
  );
}
