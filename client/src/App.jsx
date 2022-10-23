import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import React from "react";
import { LandingPage, Create } from "./components";

const App = () => (
	<Router>
		<Routes>
			<Route path="/" element={<LandingPage />} />
			<Route path="create" element={<Create />} />
		</Routes>
	</Router>
);

export default App;
