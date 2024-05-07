import userController from './user'
import familyController from './family'
import parentController from './parent'
import authController from './auth'


export const API = {
    auth:authController,
    users: userController,
    family : familyController,
    parent: parentController
}