import { RouterProvider, createBrowserRouter } from "react-router-dom";
import { Profile } from "./routes/Profile";
import { Root } from "./routes/Root";
import { AppHeader } from "./components/header/AppHeader";
import { Auth0Provider } from "@auth0/auth0-react";
import { BookingForm } from "./routes/BookingForm";

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
    path: "/booking-request/:roomId",
    element: <BookingForm />
  }
]);

export function App() {
  return (
    <Auth0Provider
      domain="" // TODO: Add your Auth0 domain
      clientId="" // TODO: Add your Auth0 client ID
      authorizationParams={{
        redirect_uri: window.location.origin
      }}
    >
      <AppHeader />
      <RouterProvider router={router} />
    </Auth0Provider>
  )
}