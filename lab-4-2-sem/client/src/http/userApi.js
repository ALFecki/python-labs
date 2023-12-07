import { $host, $authHost } from './index';
import { jwtDecode } from 'jwt-decode';


export const registration = async (login, password) => {
    try {
        const { data } = await $host.post('api/auth/register', { login, password });
        localStorage.setItem('token', data.token)
        return jwtDecode(data.token);
    } catch (e) {

        let fieldError;

        try {
            fieldError = JSON.parse(e?.response?.data?.message)
        } catch (jsonError) {
            throw (e?.response?.data?.message.split(':')[1] || "Incorrect format");
        }

        throw fieldError;
    }
}

export const login = async (login, password) => {
    try {
        const { data } = await $host.post('api/auth/login', { login, password });
        localStorage.setItem('token', data.token)

        return jwtDecode(data.token);
    } catch (e) {
        throw (JSON.parse(e?.response?.data?.message) || "Unexpected error");
    }
}

export const check = async () => {
    const { data } = await $authHost.get('api/auth');

    localStorage.setItem('token', data.token)
    return jwtDecode(data.token);
}

export const getUsers = async (roleId) => {
    const res = await $host.get('api/user', { params: { roleId } });

    const { data } = res;
    return data;
}

export const updateUser = async (id, user) => {
    const { data } = await $authHost.patch(`api/user/${id}`, user);
    return data;
}