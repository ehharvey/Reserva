import { Button, Table } from "@mantine/core"
import { useContext, useEffect, useState } from 'react';
import { TextInput } from '@mantine/core';
import { GetTokenSilentlyOptions, useAuth0 } from "@auth0/auth0-react";
import { ItemApi, Configuration, ItemsGetRequest } from "../reserva_client";
import { ConfigContext } from "../contexts/ConfigProvider";
import { useNavigate } from "react-router-dom";


interface searchParams {
  nameSearch: string;
  locationSearch: string;
  descriptionSearch: string;
}

export function Rooms() {
  const config = useContext(ConfigContext);
  const { getAccessTokenSilently, user } = useAuth0();
  const [nameSearch, setNameSearch] = useState('');
  const [locationSearch, setLocationSearch] = useState('');
  const [descriptionSearch, setDescriptionSearch] = useState('');
  const [rows, setRows] = useState<JSX.Element[]>();
  const navigate = useNavigate();

  const search = {
    nameSearch: nameSearch,
    locationSearch: locationSearch,
    descriptionSearch: descriptionSearch
  } as searchParams;

  const accessTokenOptions: GetTokenSilentlyOptions = {
    authorizationParams: {
      audience: config?.api.baseUrl,
    }
  };

  const itemApi = new ItemApi(
    new Configuration({ basePath: config?.api.baseUrl, accessToken: "Bearer " + getAccessTokenSilently(accessTokenOptions) })
  );

  useEffect(() => {
    const itemsGetRequest = {
      nameSearch: nameSearch,
      locationSearch: locationSearch,
      descriptionSearch: descriptionSearch
    } as ItemsGetRequest

    itemApi.itemsGet(itemsGetRequest).then((response) =>  {
      const rows = response.rooms?.map((item) => {
        return (
          <tr key={item.id}>
            <td>{item.name}</td>
            <td>{item.location}</td>
            <td>{item.description}</td>
            <td><Button onClick={() => navigate("/booking-request/" + item.id)}>Book</Button></td>
          </tr>
        )
      });
      setRows(rows);
    }).catch((error) => {
      console.log(error);
    });
  }, [nameSearch, locationSearch, descriptionSearch]);

  return (
    <div>
      <h1>Rooms</h1>
      <TextInput
        placeholder={"Search By Name"}
        value={nameSearch} onChange={(event) => {
          setNameSearch(event.currentTarget.value);
        }}
      />
      <TextInput
        placeholder={"Search By Location"}
        value={locationSearch} onChange={(event) => {
          setLocationSearch(event.currentTarget.value);
        }}
      />
      <TextInput
        placeholder={"Search By Description"}
        value={descriptionSearch} onChange={(event) => {
          setDescriptionSearch(event.currentTarget.value);
        }}
      />


      <Table striped highlightOnHover withBorder withColumnBorders>
        <thead>
          <tr>
            <th>Name</th>
            <th>Room Location</th>
            <th>Room Description</th>
            <th>Book</th>
          </tr>
        </thead>
        <tbody> {rows}</tbody>
      </Table>
    </div>
  )
}