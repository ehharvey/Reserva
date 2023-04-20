import { NativeSelect, Table } from "@mantine/core"
import { useState } from 'react';
import { MultiSelect } from '@mantine/core';
import { TextInput } from '@mantine/core';
import { Room } from "../entities/Room";


interface paramsObj {
  name: string;
  location: string;
  description: string;
  [key:string]: string;
}


const paramsObj: paramsObj = {
  "name": "",
  "location": "",
  "description": "",
  "type": ""
}; 

function searchAPI(searchParams:URLSearchParams) {
  const rooms = [
    {
      name: "Room 2312",
      location: "A-Wing 2nd Floor",
      description: "This is an awesome room filled with so much fun!",
      type: "Fun Room",
      features: "Friendly, Awesome whatever",
      id: 1,
      created_at: "Jan 12, 2012",
      last_updated_at: "Jan 12, 2015"
    },
    {
      name: "Room 1001",
      location: "B-Wing 1st Floor",
      description: "This room is great for studying or working alone.",
      type: "Study Room",
      features: "Quiet, Has a desk and chair",
      id: 2,
      created_at: "Feb 15, 2013",
      last_updated_at: "Feb 18, 2015"
    },
    {
      name: "Room 2020",
      location: "C-Wing 2nd Floor",
      description: "This is a cozy room with a great view of the city.",
      type: "Comfort Room",
      features: "Warm lighting, Comfortable furniture",
      id: 3,
      created_at: "Mar 22, 2014",
      last_updated_at: "Mar 24, 2016"
    },
    {
      name: "Room 305",
      location: "D-Wing 3rd Floor",
      description: "This is a large conference room that can fit up to 20 people.",
      type: "Conference Room",
      features: "Projector, Whiteboard, Conference table and chairs",
      id: 4,
      created_at: "Apr 18, 2015",
      last_updated_at: "Apr 20, 2018"
    },
    {
      name: "Room 405",
      location: "E-Wing 4th Floor",
      description: "This is a bright and airy room that's perfect for yoga or meditation.",
      type: "Fitness Room",
      features: "Large windows, Yoga mats, Meditation cushions",
      id: 5,
      created_at: "May 25, 2016",
      last_updated_at: "May 28, 2019"
    }
  ];

  const name = searchParams.get('name');
  const location = searchParams.get('location');
  const description = searchParams.get('description');

  const filteredRooms = rooms.filter((room) => {
    return Object.entries(paramsObj).reduce((result, [key, value]) => {
      if (value === "") {
        return result;
      }
      return result && room[key].toLowerCase().includes(value.toLowerCase());
    }, true);
  });
  

  const rows = filteredRooms.map((room) => {
    const theRoute = `/rooms/${room.id}`;
    return (
      <tr key={room.id} onClick={() => { window.location.href = theRoute; }}>
        <td>{room.name}</td>
        <td>{room.location}</td>
        <td>{room.description}</td>
        <td>{room.type}</td>
        <td>{room.features}</td>
        <td>{room.created_at}</td>
        <td>{room.last_updated_at}</td>
      </tr>
    );
  });

  

  return rows;
}


export function Rooms() {

  const [featureValue, setFeatureValue] = useState('name');
  const [textValue, setTextValue] = useState('');

  

paramsObj[featureValue] = textValue;
const searchParams = new URLSearchParams(paramsObj);
  


  console.log(searchParams.toString())



  const rooms = [
    {
      name: "Room 2312",
      location: "A-Wing 2nd Floor",
      description: "This is an awesome room filled with so much fun!",
      type: "Fun Room",
      features: "Friendly, Awesome whatever",
      id: 1,
      created_at: "Jan 12, 2012",
      last_updated_at: "Jan 12, 2015"
    },
    {
      name: "Room 1001",
      location: "B-Wing 1st Floor",
      description: "This room is great for studying or working alone.",
      type: "Study Room",
      features: "Quiet, Has a desk and chair",
      id: 2,
      created_at: "Feb 15, 2013",
      last_updated_at: "Feb 18, 2015"
    },
    {
      name: "Room 2020",
      location: "C-Wing 2nd Floor",
      description: "This is a cozy room with a great view of the city.",
      type: "Comfort Room",
      features: "Warm lighting, Comfortable furniture",
      id: 3,
      created_at: "Mar 22, 2014",
      last_updated_at: "Mar 24, 2016"
    },
    {
      name: "Room 305",
      location: "D-Wing 3rd Floor",
      description: "This is a large conference room that can fit up to 20 people.",
      type: "Conference Room",
      features: "Projector, Whiteboard, Conference table and chairs",
      id: 4,
      created_at: "Apr 18, 2015",
      last_updated_at: "Apr 20, 2018"
    },
    {
      name: "Room 405",
      location: "E-Wing 4th Floor",
      description: "This is a bright and airy room that's perfect for yoga or meditation.",
      type: "Fitness Room",
      features: "Large windows, Yoga mats, Meditation cushions",
      id: 5,
      created_at: "May 25, 2016",
      last_updated_at: "May 28, 2019"
    }
  ];

  var rows = searchAPI(searchParams); // searchAPI is just a dummy function 


  // var rows = rooms.map((room) => {
  //   if (room.hasOwnProperty(featureValue)) {
  //     const value = room[featureValue];

  //     const theRoute = "/rooms/"+ room.id;
      
  //     if (typeof (value) === "string" && ((value.toLowerCase().includes(textValue.toLowerCase())) || !textValue))
  //       return (

         
  //         <tr key={room.id} onClick={() => {window.location.href = theRoute;}}>
            
  //           <td> {room.name}</td>
  //           <td>{room.location}</td>
  //           <td>{room.description}</td>
  //           <td>{room.type}</td>
  //           <td>{room.features}</td>
  //           <td>{room.created_at}</td>
  //           <td>{room.last_updated_at}</td>
          
  //         </tr>
         
  //       )
  //   }
  // }
 // )


  return (
    <div>
      <h1>Rooms</h1>
      <NativeSelect
        value={featureValue}
        onChange={(event) => {
          paramsObj[featureValue]='';
          setFeatureValue(event.currentTarget.value);
          setTextValue('');
        }
        }
        data={['name', 'type', 'location', 'description']}
      />
      <TextInput
        placeholder={"type here ..."}
        label={featureValue}
        value={textValue} onChange={(event) => setTextValue(event.currentTarget.value)}
      />

      <Table striped highlightOnHover withBorder withColumnBorders>
        <thead>
          <tr>
            <th>Name</th>
            <th>Room Location</th>
            <th>Room Description</th>
            <th>Room Type</th>
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