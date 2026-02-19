import { useEffect, Fragment } from "react";
import {
  Table,
  TableHead,
  TableRow,
  TableCell,
  TableBody,
  TableContainer,
  Paper,
  Chip,
  CircularProgress,
  Typography,
} from "@mui/material";
import { useAppDispatch, useAppSelector } from "../../redux/hooks";
import { fetchIncidents } from "../../redux/thunk";
import { headers } from "./data";
import { getPriorityLabel, getStatusLabel } from "../../utils";
import NotFound from "../notFound/notfound-component";
import styles from "./dashboard.module.scss";

const DashboardComponent = () => {
  const dispatch = useAppDispatch();
  const { data, loading, error } = useAppSelector((state) => state.incidents);

  useEffect(() => {
    dispatch(fetchIncidents());
  }, [dispatch]);

  if (loading)
    return (
      <div className={styles.centerColumn}>
        <CircularProgress />
        <Typography variant="h6" color="text.secondary">
          Loading Incidents...
        </Typography>
      </div>
    );

  if (error)
    return (
      <div className={styles.centerBox}>
        <Typography className="errorText" variant="h6">
          Error: {error}
        </Typography>
      </div>
    );

  return (
    <Fragment>
      <TableContainer component={Paper} sx={{ mt: 3 }}>
        <Table>
          <TableHead>
            <TableRow>
              {headers.map((header, index) => (
                <TableCell key={index} sx={{ fontWeight: "bold" }}>
                  {header}
                </TableCell>
              ))}
            </TableRow>
          </TableHead>

          <TableBody>
            {data.length > 0 ? (
              data.map((row) => (
                <TableRow key={row.id} hover>
                  <TableCell>{row.title}</TableCell>

                  <TableCell>
                    <Chip
                      label={getStatusLabel(row.status_id)}
                      color="primary"
                      size="small"
                    />
                  </TableCell>

                  <TableCell>
                    <Chip
                      label={getPriorityLabel(row.priority_id)}
                      color="warning"
                      size="small"
                    />
                  </TableCell>

                  <TableCell>{row.description}</TableCell>

                  <TableCell>{row.title.split("\n")[0]}</TableCell>

                  <TableCell>
                    {row.ai_analysis?.root_cause} ({row.ai_analysis?.confidence}
                    )
                  </TableCell>

                  <TableCell>
                    {new Date(row.created_at).toLocaleString()}
                  </TableCell>
                </TableRow>
              ))
            ) : (
              <TableRow>
                <TableCell colSpan={7} align="center">
                  <NotFound />
                </TableCell>
              </TableRow>
            )}
          </TableBody>
        </Table>
      </TableContainer>
    </Fragment>
  );
};

export default DashboardComponent;
