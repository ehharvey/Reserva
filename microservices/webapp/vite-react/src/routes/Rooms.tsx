import { Table } from "@mantine/core"
import { useState } from 'react';
import { TextInput } from '@mantine/core';


interface searchParams {
  name: string;
  location: string;
  description: string;
}

function searchAPI(search: searchParams) {
  const rooms = [
    {
      name: "Room 2312",
      location: "A-Wing 2nd Floor",
      description: "This is an awesome room filled with so much fun!",
      type: "Room",
      features: "Friendly, Awesome whatever",
      id: 1,
      created_at: "Jan 12, 2012",
      last_updated_at: "Jan 12, 2015"
    },
    {
      name: "Room 1001",
      location: "B-Wing 1st Floor",
      description: "This room is great for studying or working alone.",
      type: "Room",
      features: "Quiet, Has a desk and chair",
      id: 2,
      created_at: "Feb 15, 2013",
      last_updated_at: "Feb 18, 2015"
    },
    {
      name: "Room 2020",
      location: "C-Wing 2nd Floor",
      description: "This is a cozy room with a great view of the city.",
      type: "Room",
      features: "Warm lighting, Comfortable furniture",
      id: 3,
      created_at: "Mar 22, 2014",
      last_updated_at: "Mar 24, 2016"
    },
    {
      name: "Room 305",
      location: "D-Wing 3rd Floor",
      description: "This is a large conference room that can fit up to 20 people.",
      type: "Room",
      features: "Projector, Whiteboard, Conference table and chairs",
      id: 4,
      created_at: "Apr 18, 2015",
      last_updated_at: "Apr 20, 2018"
    },
    {
      name: "Room 405",
      location: "E-Wing 4th Floor",
      description: "This is a bright and airy room that's perfect for yoga or meditation.",
      type: "Room",
      features: "Large windows, Yoga mats, Meditation cushions",
      id: 5,
      created_at: "May 25, 2016",
      last_updated_at: "May 28, 2019"
    }
  ];

  const filteredRooms = rooms.filter((room) => {
    return Object.entries(search).reduce((result, [key, value]) => {
      if (typeof(key)!== "string" || value === "") {
        return result;
      }
      return result && (room[key as keyof typeof room || '']).toString().toLowerCase().includes(value.toLowerCase());
    }, true);
  });
  

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
  const [nameSearch, setNameSearch] = useState('');
  const [locationSearch, setLocationSearch] = useState('');
  const [descriptionSearch, setDescriptionSearch] = useState('');

  const search = {
    name: nameSearch,
    location: locationSearch,
    description: descriptionSearch
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