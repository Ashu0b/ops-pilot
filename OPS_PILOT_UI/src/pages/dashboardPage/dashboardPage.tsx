import { Fragment } from "react/jsx-runtime";
import DashboardComponent from "../../components/dashboard/dashboard-component";
import styles from "./dashboardPage.module.scss";

const DashboardPage = () => {
  return (
    <Fragment>
      <div className={styles.headerWrpper}>
        <h1>Dashboard of Devops Incident</h1>
        <button className={styles.addBtn}> Add Incident</button>
      </div>
      <DashboardComponent />
    </Fragment>
  );
};

export default DashboardPage;
