import React from "react";
import { Config } from "../entities/Config";

// Create a context for the config
export const ConfigContext = React.createContext<Config | null>(null);