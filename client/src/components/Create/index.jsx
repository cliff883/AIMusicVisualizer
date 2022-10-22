import React, { useState } from "react";
import Upload from "./Upload";
import Download from "./Download";
import Loading from "./Loading/Loading";

const Create = () => {
	const [state, setState] = useState({
		status: "upload",
	});

	const handleUpload = () => {
		console.log("handling upload");
		setState({ ...state, status: "loading" });
	};
	const handleDownload = () => {
		console.log("handling download");
	};

	const renderSwitch = (s) => {
		console.log(s);
		switch (s) {
			case "loading":
				return <Loading />;
			case "done":
				return <Download handleDownload={handleDownload} />;
			case "upload":
			default:
				return <Upload handleUpload={handleUpload} />;
		}
	};
	return (
		<section id="c-main">
			<div className="flex h-screen justify-center items-center bg-primary">
				<div className="m-auto">{renderSwitch(state.status)}</div>
			</div>
		</section>
	);
};

export default Create;
