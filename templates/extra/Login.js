import { useState } from "react";
import { useDispatch } from "react-redux";
import { Link, useNavigate } from "react-router-dom";
import { toast } from "react-toastify";
import { setUser, setisLogged } from "../../rtk/slices/user-slice";
import UserServices from "../../service/UserServices";

import './Login.css';

const Login = () => {

    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")

    const dispatch = useDispatch();
    const navigate = useNavigate();

    const handleSubmit = async () => {
        try {
            if (email !== "" && password !== "") {
                const req = await UserServices.login({ email: email, password: password });
                if (req.status === 200) {
                    const user = req?.data;
                    dispatch(setUser(user));
                    dispatch(setisLogged(true));
                    localStorage.setItem('user', JSON.stringify(user));
                    navigate('/');
                }
            } else {
                toast.warning('Email or Password Should Not Be Empty');
            }
        }
        catch (error) {
            toast.error(error.response?.data?.message || error.message);
        }
    }

    return (
        <section className="login">
            <div className="container">
                <div className="row d-flex justify-content-center align-items-center">
                    <div className="col-12 col-md-6 col-lg-7">
                        <img src="./assets/images/signin.jpg" alt="login" className="img-fluid h-100 w-100" />
                    </div>
                    <div className="col-12 col-md-6 col-lg-5">
                        <h2 className="text-center fw-bold" style={{ color: '#263238', letterSpacing: '4px' }}>WELCOME</h2>
                        <div className="card-body p-4 p-lg-5">
                            <div className="input-group mb-3">
                                <span className="input-group-text">
                                    <i className="fa-solid fa-user fa-xl" style={{ color: "#0d6efd" }}></i>
                                </span>
                                <div className="form-floating">
                                    <input type="email" id="email" className="form-control"
                                        value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Email" />
                                    <label htmlFor="email" style={{ color: '#aaaaaa' }}>Email</label>
                                </div>
                            </div>
                            <div className="input-group mb-3">
                                <span className="input-group-text">
                                    <i className="fa-solid fa-lock fa-xl" style={{ color: "#0d6efd" }}></i>
                                </span>
                                <div className="form-floating">
                                    <input type="password" id="password" className="form-control" value={password}
                                        onChange={(e) => setPassword(e.target.value)} placeholder="Password" />
                                    <label htmlFor="password" style={{ color: '#aaaaaa' }}>Password</label>
                                </div>
                            </div>
                            <p className="text-end mb-4" style={{ color: '#aaaaaa', fontSize: '14px' }}>Forget Password ?</p>
                            <div className="mb-2 text-center">
                                <button type="button" className="btn btn-lg" style={{ color: '#ffffff', padding: '8px 70px', backgroundColor: '#0d6efd', borderRadius: '40px', letterSpacing: '2px' }} onClick={handleSubmit}>LOGIN</button>
                            </div>
                            <p className="mb-4 pb-lg-3 text-center" style={{ color: '#7a7a7a' }}> Don't have an account?{" "}
                                <Link to="/register" style={{ color: '#0d6efd' }}>
                                    Register here
                                </Link>
                            </p>
                            <div className="text-center">
                                <Link to='/' className="btn" style={{ color: '#0d6efd', padding: '8px 50px', backgroundColor: '#ffffff', border: '2px solid #D3D3D3', borderRadius: '40px' }}>Back</Link>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    );
}

export default Login;