import { useState } from "react";
import { components } from "../entities/schema";

async function fetchItems(search: components["schemas"]["UpdateItem"]) {
    
}

export function ItemSearch() {
    const [search, setSearch] = useState<components["schemas"]["UpdateItem"] | undefined>(undefined);
    const [items, setItems] = useState<components["schemas"]["Item"][]>([]);
    const [loading, setLoading] = useState(false);
    
    const searchRooms = async () => {
        if (!search) return;

        setLoading(true);
        const rooms = await fetchItems(search);
        setItems(items);
        setLoading(false);
    };
}