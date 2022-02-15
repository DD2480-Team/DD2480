import React from "react";
import {
  SectionContentContainer,
  ListItemBox,
  ListItemKey,
  ListItemValue,
} from "./ListItemStyles";

export const ListItem = ({ build }) => {
  if (!build) {
    return null;
  }

  const buildInformation = {
    ID: build.id,
    Branch: build.branch,
    Owner: build.owner,
    Pusher: build.pusher,
    Repository: build.repo_name,
    Status: build.syntax_result ? "Success" : "Failure",
    Test_Result: build.test_result ? "Success" : "Failure", 
    Timestamp: new Date(build.timestamp * 1000).toString().split("GMT")[0],
  };

  return (
    <SectionContentContainer>
      {Object.keys(buildInformation).map((key, idx) => {
        return (
          <ListItemBox key={idx}>
            <ListItemKey>{key}</ListItemKey>
            <ListItemValue>{buildInformation[key]}</ListItemValue>
          </ListItemBox>
        );
      })}
    </SectionContentContainer>
  );
};
