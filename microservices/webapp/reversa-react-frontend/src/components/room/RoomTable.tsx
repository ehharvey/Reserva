import React from "react";
import { Column, useTable, TableInstance } from "react-table";
import { Room } from "../../entities/Room";
import { Feature } from "../../entities/Feature";
import "./RoomTable.css"

interface Props {
  data: Room[];
}

export function RoomTable({ data }: Props) {

  // Define columns using useMemo
  const columns = React.useMemo<Column<Room>[]>(
    () => [
      {
        Header: "ID",
        accessor: "id", // accessor is the "key" in the data
      },
      {
        Header: "Name",
        accessor: "name",
      },
      {
        Header: "Location",
        accessor: "location",
        Cell: ({ value }) => {
          return <span>{value.name}</span>; // Render the nested "name" property of "location"
        },
      },
      {
        Header: "Size",
        accessor: "size",
        Cell: ({ value }) => {
          return <span>{value}</span>;
        },
      },
      {
        Header: "Features",
        accessor: "features",
        Cell: ({ value }: { value: Array<Feature> }) => {
          return (
            <ul>
              {value.map((feature) => (
                <li>{feature.name}</li> // Render each feature's name in a bullet point list
              ))}
            </ul>
          );
        },
      },
      {
        Header: "Image",
        accessor: "image_url",
        Cell: ({ value }) => {
          return <img src={value} alt="Room" style={{ width: '200px', height: '200px' }} />;
        },
      },
    ],
    []
  );

  // Use useTable hook to create table instance and extract needed properties
  const { getTableProps, getTableBodyProps, headerGroups, rows, prepareRow } =
    useTable<Room>({ columns, data }) as TableInstance<Room>;

  return (
    <div className = "table-container">
      <div className="table-title">Available Rooms</div>

      {/* Render table with its headers and body */}
      <table {...getTableProps()}>
        <thead>
          {headerGroups.map((headerGroup) => (
            <tr {...headerGroup.getHeaderGroupProps()}>
              {headerGroup.headers.map((column) => (
                <th {...column.getHeaderProps()}>{column.render("Header")}</th> // Render column header
              ))}
            </tr>
          ))}
        </thead>
        <tbody {...getTableBodyProps()}>
          {rows.map((row) => {
            prepareRow(row); // Prepare row for rendering
            return (
              <tr {...row.getRowProps()}>
                {row.cells.map((cell) => (
                  <td {...cell.getCellProps()}>{cell.render("Cell")}</td> // Render cell data
                ))}
              </tr>
            )
          })}
        </tbody>
      </table>
    </div>
  );
}
