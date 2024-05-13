import { useAlertStore } from "./alert"
import { useAuthStore } from "./auth"
import { useFamilyStore } from "./family"
import { useUserStore } from "./user"

export default function reset_all_stores(){
    useFamilyStore().$reset()
    useUserStore().$reset()
    useAlertStore().$reset()
    useAuthStore().$reset()

}