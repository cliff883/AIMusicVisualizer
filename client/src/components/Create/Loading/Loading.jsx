import React from "react";
import "mathsass";
import "./loading.scss";

const Loading = () => (
	<div className="flex justify-center align-middle items-center">
		<div className="flex justify-center absolute">
			<div className="spinner"></div>
		</div>
		<h1 className="font-sans font-extrabold text-[50px] absolute">
			working on it.
		</h1>
	</div>
);

export default Loading;
