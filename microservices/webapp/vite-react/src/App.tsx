import { RouterProvider, createBrowserRouter } from "react-router-dom";
import { Root } from "./routes/Root";
import { Profile } from "./routes/Profile";
import { Groups } from "./routes/Groups";
import { AppHeader } from "./components/header/AppHeader";
import { Auth0Provider } from "@auth0/auth0-react";
import { Rooms } from "./routes/Rooms";
import { BookingForm } from "./routes/BookingForm";
import { BookingList } from "./routes/BookingList";
import { ConfigContext } from "./contexts/ConfigProvider";
import { useContext } from "react";
import { Config } from "./entities/Config";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Root />,
  },
  {
    path: "/me",
    element: <Profile />
  }, 
  {
    path: "/rooms",
    element: <Rooms />
  },
  {
    path: "/bookings",
    element: <BookingList />
  },
  {
    path: "/groups",
    element: <Groups />
  },
  {
    path: "/booking-request/:roomId",
    element: <BookingForm />
  }
]);

export function App() {
  const config = {
    auth0: {
      domain: import.meta.env.VITE_AUTH_DOMAIN,
      clientId: import.meta.env.VITE_AUTH_CLIENT_ID
    },
    api: {
      baseUrl: import.meta.env.VITE_API_BASE_URL
    }
  } as Config;
  
  return (
    <Auth0Provider
      domain={import.meta.env.VITE_AUTH_DOMAIN}
      clientId={import.meta.env.VITE_AUTH_CLIENT_ID}
      authorizationParams={{
        redirect_uri: window.location.origin
      }}
    >
      <ConfigContext.Provider value={config}>
        <AppHeader />
        <RouterProvider router={router} />
      </ConfigContext.Provider>
    </Auth0Provider>
  )
}