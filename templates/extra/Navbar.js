import { useNavigate, NavLink, Link } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { logout } from '../../rtk/slices/user-slice';
import './Navbar.css';

const Navbar = () => {

    const dispatch = useDispatch();
    const navigate = useNavigate();

    const isLogged = useSelector((state) => state.user.isLogged);
    const user = useSelector((state) => state.user.user);
    const cartLeng = useSelector(state => state.cart);


    const handleLogout = () => {
        dispatch(logout());
        navigate('/');
    }

    return (
        <nav className="navbar navbar-expand-lg py-3">
            <div className="container">
                {/* <NavLink className="navbar-brand" to="/">WizoCell</NavLink> */}
                <button className="navbar-toggler shadow-none" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasNavbar" aria-controls="offcanvasNavbar" aria-label="Toggle navigation">
                    <i className="fa-solid fa-bars"></i>
                </button>
                <div className="offcanvas offcanvas-start" tabIndex="-1" id="offcanvasNavbar" aria-labelledby="offcanvasNavbarLabel">
                    <div className="offcanvas-header">
                        <h5 className="offcanvas-title" id="offcanvasNavbarLabel">Hello User</h5>
                        <button type="button" className="btn-close shadow-none" data-bs-dismiss="offcanvas" aria-label="Close"></button>
                    </div>
                    <div className="offcanvas-body">
                        <ul className="navbar-nav justify-content-start flex-grow-1 pe-3 gap-2 gap-lg-4">
                            <li className="nav-item">
                                <NavLink className="nav-link" to="/">Home</NavLink>
                            </li>
                            <li className="nav-item">
                                <NavLink className="nav-link" to="/alfa">Alfa</NavLink>
                            </li>
                            <li className="nav-item">
                                <NavLink className="nav-link" to="/touch">Touch</NavLink>
                            </li>
                            <li className="nav-item">
                                <NavLink className="nav-link" to="/about">About Us</NavLink>
                            </li>
                            <li className="nav-item">
                                <NavLink className="nav-link" to="/contact">Contact Us</NavLink>
                            </li>
                        </ul>
                    </div>
                </div>
                <div className='d-flex align-items-center'>
                    {/* <span className='fw-bold'>
                        Balance: {user?.balance || 0} LL
                    </span> */}
                    {isLogged &&
                        <Link to="/cart">
                            <button type="button" className="btn position-relative">
                                <i className="fa-solid fa-cart-shopping" style={{ fontSize: "20px" }}></i>
                                <span className="position-absolute top-0 start-100 translate-middle badge rounded-pill badge-notification bg-primary">
                                    {cartLeng.length}
                                </span>
                            </button>
                        </Link>
                    }
                    <div className="dropdown">
                        <button className="btn dropdown-toggle border-0 hidden-arrow" type="button" data-bs-toggle="dropdown"
                            data-bs-auto-close="true" aria-expanded="false">
                            <img src="https://mdbcdn.b-cdn.net/img/new/avatars/2.webp" className="rounded-circle"
                                height="30" alt="avatar"
                            />
                        </button>
                        <ul className="dropdown-menu dropdown-menu-end">
                            {/* {isLogged ?
                                <li className="nav-item dropdown">
                                    <ul className="dropdown-menu">
                                        <li><NavLink className="dropdown-item" to="/orders">My Orders</NavLink></li>
                                        <li><button className="btn dropdown-item" onClick={handleLogout} >Logout</button></li>
                                    </ul>
                                </li> :
                                <>
                                    <li className="nav-item">
                                        <NavLink className="nav-link" to="/register">Register</NavLink>
                                    </li>
                                    <li className="nav-item">
                                        <NavLink className="nav-link" to="/login">Login</NavLink>
                                    </li>
                                </>
                            } */}
                            {isLogged ? (
                                <>
                                    <li className='dropdown-item'>
                                        <span className='fw-bold'>
                                            Balance: {user?.balance || 0} LL
                                        </span>
                                    </li>
                                    <li className='dropdown-item'>
                                        <NavLink className="nav-link" to="/orders">My Orders</NavLink>
                                    </li>
                                    <li className='dropdown-item'>
                                        <button className="btn" onClick={handleLogout} >Logout</button>
                                    </li>
                                </>
                            ) : (
                                <>
                                    <li className="dropdown-item">
                                        <NavLink className="nav-link" to="/register">Register</NavLink>
                                    </li>
                                    <li className="dropdown-item">
                                        <NavLink className="nav-link" to="/login">Login</NavLink>
                                    </li>
                                </>
                            )}
                        </ul>
                    </div>
                </div>
            </div>
        </nav>
    )
}

export default Navbar;