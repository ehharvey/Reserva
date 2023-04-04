import React, { useState } from "react";
import { Container, Row, Col, Button, Table, Card, Dropdown } from "react-bootstrap";
import WeeklyView from "./WeeklyView";
import CardHeader from "react-bootstrap/esm/CardHeader";

export function AvailabilityScheduler() {

    return (
        <Container>
            <Row>
                <Card className="mb-3">
                    <Card.Body>
                        <Card.Title>
                            Availability Scheduler
                        </Card.Title>
                        <Row>
                            <Col>
                                <Card.Text>Scheduler Type</Card.Text>
                                <select>
                                    <option value="">Base - All Time</option>
                                    <option value="">Base - Date Specific</option>
                                    <option value="">Room - All Time</option>
                                    <option value="">Room - Date Specific</option>
                                </select>
                            </Col>
                            <Col>
                                <Card.Text>Room</Card.Text>
                                <select>
                                    <option value="">Room 1A01</option>
                                    <option value="">Base - Overwrite</option>
                                    <option value="">Room Default</option>
                                    <option value="">Room Default - Overwrite</option>
                                </select>
                            </Col>
                            <Col>
                                <Card.Text>Settings</Card.Text>
                                <label>
                                    <input type="checkbox" name="remember_me_checkbox" id="remember_me_checkbox" />
                                    Priority
                                </label>
                            </Col>
                        </Row>
                    </Card.Body>
                </Card>
            </Row>

            <Row>
                <WeeklyView />
            </Row>

        </Container>


    )
}