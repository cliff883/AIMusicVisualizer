import React, { useState } from "react";
import axios from "axios";
import Upload from "./Upload";
import Download from "./Download";
import Loading from "./Loading/Loading";

const UPLOAD_URL = "http://localhost:8080/api/upload/song";
const DOWNLOAD_URL = "http://localhost:8080/api/download/video?alt=media";

const Create = () => {
	const [state, setState] = useState({
		status: "upload",
	});

	const handleUpload = async (e) => {
		console.log("handling upload");
		const formData = new FormData();
		formData.append("in_file", e.target.files[0]);
		axios
			.post(UPLOAD_URL, formData)
			.then((res) => {
				setState({ ...state, status: "loading" });
			})
			.catch((err) => {
				console.log(err);
				alert("File Upload Error");
			});
	};

	const handleDownload = () => {
		console.log("handling download");
		axios({ url: DOWNLOAD_URL, method: "GET", responseType: "blob" })
			.then((res) => {
				console.log(res);
				const url = URL.createObjectURL(res.data);
				const link = document.createElement("a");
				link.href = url;
				link.setAttribute("download", "output.mp4");
				document.body.appendChild(link);
				link.click();
				link.parentNode.removeChild(link);
			})
			.catch((err) => {
				console.log(err);
				alert("File Download Error");
			});
	};

	const renderSwitch = (s) => {
		switch (s) {
			case "loading":
				return <Loading setState={setState} />;
			// return <Download handleDownload={handleDownload} />;
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
