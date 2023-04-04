import React, { useState } from "react";
import { Container, Row, Col, Button, Table, Card } from "react-bootstrap";



function WeeklyView() {
    const [date, setDate] = useState(new Date());

    // Helper function to get the start and end date of the week
    const getStartAndEndDateOfWeek = (date: Date) => {
        const dayOfWeek = date.getDay();
        const startDate = new Date(date);
        startDate.setDate(startDate.getDate() - dayOfWeek);
        startDate.setHours(0, 0, 0, 0);
        const endDate = new Date(startDate);
        endDate.setDate(endDate.getDate() + 6);
        endDate.setHours(23, 59, 59, 999);
        return { startDate, endDate };
    };

    // Generate the table rows for the calendar
    let rows = [];
    let cells = [];

    // Get the start and end date of the week
    const { startDate, endDate } = getStartAndEndDateOfWeek(date);

    // Loop through the 8 hours of each day in the week
    for (let hour = 0; hour < 8; hour++) {
        cells = [];
        for (let i = 0; i < 7; i++) {
            const day = new Date(startDate);
            day.setDate(day.getDate() + i);
            const formattedDay = day.toLocaleDateString("en-US", { weekday: "short" });
            const formattedDate = day.toLocaleDateString("en-US", { day: "numeric" });
            const className = hour === 0 ? "border-top" : "";
            cells.push(
                <td key={i} className={className}>
                    <div className="hour">{hour + 8}:00</div>
                    <div className="events">Events for {formattedDay} ({formattedDate})</div>
                </td>
            );
        }
        rows.push(<tr key={hour}>{cells}</tr>);
    }

    const [selectedCells, setSelectedCells] = useState<number[][]>([]);

    const handleCellClick = (rowIndex: number, columnIndex: number) => {
        // Check if the clicked cell is already selected
        const isSelected = selectedCells.some(
            ([selectedRowIndex, selectedColumnIndex]) =>
                selectedRowIndex === rowIndex && selectedColumnIndex === columnIndex
        );

        if (isSelected) {
            // If the clicked cell is already selected, remove it from the selected cells array
            setSelectedCells((prevSelectedCells) =>
                prevSelectedCells.filter(
                    ([selectedRowIndex, selectedColumnIndex]) =>
                        !(selectedRowIndex === rowIndex && selectedColumnIndex === columnIndex)
                )
            );
        } else {
            // If the clicked cell is not selected, add it to the selected cells array
            setSelectedCells((prevSelectedCells: number[][]) => {
                const newSelectedCells = [...prevSelectedCells, [rowIndex, columnIndex]];
                return newSelectedCells;
            });
        }
    };

    return (
        <Container>
            <Card>
                <Card.Body>
                    <Row>
                        <Col>
                            <h3>
                                Week of{" "}
                                {startDate.toLocaleDateString("en-US", { month: "long", day: "numeric" })} -{" "}
                                {endDate.toLocaleDateString("en-US", { month: "long", day: "numeric" })}
                            </h3>
                        </Col>
                    </Row>
                    <Row>
                        <Col>
                            <Button onClick={() => setDate(new Date(date.getFullYear(), date.getMonth(), date.getDate() - 7))}>
                                Prev
                            </Button>
                        </Col>
                        <Col className="text-right d-flex justify-content-end">
                            <Button onClick={() => setDate(new Date(date.getFullYear(), date.getMonth(), date.getDate() + 7))}>
                                Next
                            </Button>
                        </Col>
                    </Row>
                    <Row>
                        <Col>
                            <div style={{ height: "50px", overflow: "hidden", position: "sticky", top: "0" }}>
                                <Table bordered className="mt-2">
                                    <thead>
                                        <tr>
                                            <th className="border-0" style={{ width: "50px" }}>Time</th>
                                            {Array.from({ length: 7 }, (_, i) => {
                                                const day = new Date(startDate);
                                                day.setDate(day.getDate() + i);
                                                return (
                                                    <th key={i} className="border-0" style={{ width: "50px" }}>
                                                        {day.toLocaleDateString("en-US", { weekday: "short" })}
                                                    </th>
                                                );
                                            })}
                                        </tr>
                                    </thead>
                                </Table>
                            </div>

                            <div style={{ height: "400px", overflowY: "scroll" }}>
                                <Table bordered>
                                    <tbody>
                                        {Array.from({ length: 24 }, (_, i) => (
                                            <tr key={i} style={{ height: "50px" }}>
                                                <td style={{ width: "50px" }}>{`${i}:00`}</td>
                                                {Array.from({ length: 7 }, (_, j) => {
                                                    return (
                                                        <td
                                                            style={{ width: "50px" }}
                                                        ></td>
                                                    );
                                                })}
                                            </tr>
                                        ))}
                                    </tbody>
                                </Table>
                            </div>
                        </Col>
                    </Row>
                </Card.Body>

            </Card>
        </Container>
    );
}

export default WeeklyView;

