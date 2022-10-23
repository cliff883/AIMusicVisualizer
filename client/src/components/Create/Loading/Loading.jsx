import React from "react";
import "mathsass";
import "./loading.scss";

const CHECK_URL = "http://localhost:8080/api/download/available";

const Loading = (props) => {
	const { setState } = props;

	useEffect(() => {
		axios({ url: CHECK_URL, method: "GET", timeout: 60000 })
			.then((res) => {
				setState({ ...state, status: "done" });
			})
			.catch((err) => {
				console.log(err);
				alert("File Generation Error");
			});
	}, []);

	return (
		<div className="flex justify-center align-middle items-center">
			<div className="flex justify-center absolute">
				<div className="spinner"></div>
			</div>
			<h1 className="font-sans font-extrabold text-[50px] absolute">
				working on it.
			</h1>
		</div>
	);
};

export default Loading;
