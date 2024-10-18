import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import './Header.css';  // You can add some CSS to style your header

function Header() {
  const navigate = useNavigate();

  return (
    <header className="header">
      <nav className="navbar">
        <ul>
          <li>
            <button onClick={() => navigate('/')}>Upload</button>
          </li>
          <li>
            <button onClick={() => navigate('/results')}>Results</button>
          </li>
        </ul>
      </nav>
    </header>
  );
}

export default Header;
