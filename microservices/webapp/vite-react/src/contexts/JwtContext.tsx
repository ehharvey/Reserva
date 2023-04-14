import { createContext } from 'react';

export interface JwtContext {
    jwt: string | undefined;
    setJwt: (jwt: string | undefined) => void;
}

export const JwtContext = createContext<JwtContext>({
    jwt: undefined,
    setJwt: () => {}
});