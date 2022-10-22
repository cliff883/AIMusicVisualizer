import React from "react";
import styles from "../../styles";

import astronaut from "../../assets/astronaut.png";

const Hero = () => (
	<section
		id="h-hero"
		className={`flex md:flex-row flex-col ${styles.paddingY}`}
	>
		<div
			className={`flex-1 ${styles.flexStart} flex-col xl:px-0 sm:px-16 px-6`}
		>
			<div className="flex flex-row justify-between items-center w-full">
				<h1 className="flex-1 font-sans font-semibold ss:text-[60px] text-[40px]">
					Dreams do come true.
				</h1>
			</div>
			<p className={`${styles.paragraph} max-w-[470px] mt-5 text-black`}>
				Lorem ipsum dolor sit, amet consectetur adipisicing elit. Ad
				ipsum qui modi rem incidunt nihil, perferendis temporibus
				nesciunt dolores molestias pariatur dolor repellat ut excepturi!
				Maxime eius ipsa perspiciatis possimus!
			</p>
		</div>

		<div
			className={`flex-1 flex ${styles.flexCenter} md:my-0 my-10 relative`}
		>
			<img
				src={astronaut}
				alt="billing"
				className="w-[80%] h-[100%] relative z-[5]"
			/>

			<div className="absolute z-[0] w-[40%] h-[35%] top-0 pink__gradient" />
			<div className="absolute z-[1] w-[80%] h-[80%] rounded-full white__gradient bottom-40" />
			<div className="absolute z-[0] w-[50%] h-[50%] right-20 bottom-20 blue__gradient" />
		</div>
	</section>
);

export default Hero;
