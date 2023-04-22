import { Table } from "@mantine/core"
import { useState } from 'react';
import { TextInput } from '@mantine/core';
import { useAuth0 } from "@auth0/auth0-react";


interface searchParams {
  nameSearch: string;
  locationSearch: string;
  descriptionSearch: string;
}

function searchAPI(search: searchParams) {
  

  const rows = filteredRooms.map((room) => {
    const theRoute = `/rooms/${room.id}`;
    return (
      <tr key={room.id} onClick={() => { window.location.href = theRoute; }}>
        <td>{room.name}</td>
        <td>{room.location}</td>
        <td>{room.description}</td>
        <td>{room.features}</td>
        <td>{room.created_at}</td>
        <td>{room.last_updated_at}</td>
      </tr>
    );
  });

  

  return rows;
}


export function Rooms() {
  const { getAccessTokenSilently, user } = useAuth0();
  const [nameSearch, setNameSearch] = useState('');
  const [locationSearch, setLocationSearch] = useState('');
  const [descriptionSearch, setDescriptionSearch] = useState('');

  const search = {
    nameSearch: nameSearch,
    locationSearch: locationSearch,
    descriptionSearch: descriptionSearch
  } as searchParams;

  var rows = searchAPI(search); // searchAPI is just a dummy function 


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
            <th>Room Features </th>
            <th>Room Created At</th>
            <th>Room Last Updated At</th>
          </tr>
        </thead>
        <tbody> {rows}</tbody>
      </Table>
    </div>
  )
}