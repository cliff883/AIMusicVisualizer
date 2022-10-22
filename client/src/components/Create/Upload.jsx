import React from "react";

const Upload = (props) => {
	const { handleUpload } = props;
	return (
		<div className="flex justify-center">
			<div class="flex justify-center items-center w-[30rem]">
				<label
					for="dropzone-file"
					class="flex flex-col justify-center items-center w-full h-64 bg-transparent rounded-lg border-2 border-black border-dashed cursor-pointer hover:bg-gray-200"
				>
					<div class="flex flex-col justify-center items-center pt-5 pb-6">
						<svg
							xmlns="http://www.w3.org/2000/svg"
							fill="none"
							viewBox="0 0 24 24"
							strokeWidth={1.5}
							stroke="currentColor"
							className="w-6 h-6"
						>
							<path
								strokeLinecap="round"
								strokeLinejoin="round"
								d="M3 16.5v2.25A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75V16.5m-13.5-9L12 3m0 0l4.5 4.5M12 3v13.5"
							/>
						</svg>
						<p class="mb-2 text-sm text-black">
							<span class="font-semibold">Click to upload</span>{" "}
							or drag and drop
						</p>
						<p class="text-xs text-gray-700">.mp3 only</p>
					</div>
					<input
						onChange={handleUpload}
						id="dropzone-file"
						type="file"
						accept="audio/mp3"
						class="hidden"
					/>
				</label>
			</div>
		</div>
	);
};

export default Upload;
