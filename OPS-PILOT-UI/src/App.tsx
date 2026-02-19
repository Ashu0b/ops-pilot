import { Navigate, Route, Routes } from "react-router-dom";
import DashboardPage from "./pages/dashboardPage/dashboardPage";
import NotFound from "./components/notFound/notfound-component";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Navigate to="/dashboard" replace />} />

      <Route path="/dashboard" element={<DashboardPage />} />

      <Route path="*" element={<NotFound />} />
    </Routes>
  );
}

export default App;
