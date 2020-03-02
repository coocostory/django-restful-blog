/* import {
    request
} from './request'
 */

import axios from 'axios'

const instance = axios.create({
    baseURL: 'http://127.0.0.1:8000',
    timeout: 1000,
    headers: {
        'Authorization': 'Token e6d9424f25983fe3b765651424a42aa503932539'
    }
});

export function getCourse() {
    return instance({
        url: '/course'
    })
}

export function getBlog() {
    return instance({
        url: '/blog'
    })
}