import React from "react";
import { FaFacebook, FaTwitter, FaInstagram, FaLinkedin } from "react-icons/fa";
import "../assets/css/footer.css";

const Footer: React.FC = () => {
    return (
        <footer className="footer">
            <div className="footer-content">
                <h1>TuxTech</h1>
                <p>
                    TuxTech is your one-stop shop for all your tech needs. We provide a
                    wide range of products from various categories such as computers,
                    smartphones, accessories, and much more.
                </p>

                <div className="social-links">
                    <a
                        href="https://www.facebook.com/TuxTech"
                        target="_blank"
                        rel="noreferrer"
                    >
                        <FaFacebook />
                    </a>
                    <a
                        href="https://www.twitter.com/TuxTech"
                        target="_blank"
                        rel="noreferrer"
                    >
                        <FaTwitter />
                    </a>
                    <a
                        href="https://www.instagram.com/TuxTech"
                        target="_blank"
                        rel="noreferrer"
                    >
                        <FaInstagram />
                    </a>
                    <a
                        href="https://www.linkedin.com/TuxTech"
                        target="_blank"
                        rel="noreferrer"
                    >
                        <FaLinkedin />
                    </a>
                </div>
            </div>
        </footer>
    );
};

export default Footer;
