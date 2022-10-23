import React from "react";
import Navbar from "./Navbar";
import Hero from "./Hero";
import styles from "../../styles";

const LandingPage = () => (
	<section id="h-landing">
		<div className="bg-primary w-full">
			<div className={`${styles.paddingX} ${styles.flexCenter}`}>
				<div className={`${styles.boxWidth}`}>
					<Navbar />
				</div>
			</div>
			<div className={`${styles.paddingX}`}>
				<div
					className={`flex flex-grow w-[40%] border-t-2 border-black`}
				></div>
			</div>
			<div className={`bg-primary h-screen ${styles.flexStart}`}>
				<div className={`${styles.paddingX} ${styles.boxWidth}`}>
					<Hero />
				</div>
			</div>
		</div>
	</section>
);

export default LandingPage;
