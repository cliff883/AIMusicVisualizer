import { React, useState } from "react";
// import { close, gtlogo, menu } from "../../assets";
import close from "../../assets/close.svg";
import gtlogo from "../../assets/gtlogo.svg";
import menu from "../../assets/menu.svg";

const Navbar = () => {
	return (
		<section id="h-navbar">
			<nav className="w-full flex py-6 justify-between items-center navbar">
				<div className="flex justify-start">
					{/* <img
						src={gtlogo}
						alt="logo"
						className="w-[124px] h-[32px]"
					/> */}
					<h1 className="font-sans font-extrabold text-[40px] text-[#5b7c99]">
						reverie34
					</h1>
				</div>
				<ul className="list-none flex justify-end items-center flex-1">
					<li className="font-sans font-semibold cursor-pointer mr-10 text-[16px]">
						<a href={`/create`}>get started.</a>
					</li>
				</ul>
			</nav>
		</section>
	);
};

export default Navbar;
