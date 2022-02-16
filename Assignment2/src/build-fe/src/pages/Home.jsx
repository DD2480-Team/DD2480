import React, { useEffect, useState } from "react";
import { MainPage, SectionMainHeading } from "./HomeStyles";
import { ListItem } from "../components/ListItem";
import axios from "axios";

const Home = () => {
  const [builds, setBuilds] = useState([]);

  useEffect(() => {
    const getListOfBuilds = async () => {
      try {
        const buildsArray = await axios.get(
          `${process.env.REACT_APP_SERVER_URL}/history`
        );
        setBuilds(buildsArray.data["builds"]);
      } catch (err) {
        throw new Error("could not get history of previous builds");
      }
    };
    getListOfBuilds();
  }, []);

  return (
    <MainPage>
      <SectionMainHeading>Build History</SectionMainHeading>
      <SectionMainHeading>
        Click on the boxes to see the output
      </SectionMainHeading>

      {builds
        .map((build, idx) => {
          return <ListItem build={build} key={build.timestamp} />;
        })
        .reverse()}
    </MainPage>
  );
};

export default Home;
