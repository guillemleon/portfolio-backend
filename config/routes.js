import EmailController from "../src/controllers/Controller";
import server from "./server";

const emailController = new EmailController();

export default (server) => {
    server.post(`/api/contact`, emailController.sendEmail);
    server.get('/', (req, res) => {
        res.send("HELLO WORLD")
    })
}